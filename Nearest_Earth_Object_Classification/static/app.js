document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("predict-form");
    const resultContainer = document.getElementById("result-container");

    if (form) {
        form.addEventListener("submit", async function(e) {
            e.preventDefault(); // Prevent page reload

            // Gather values from the form inputs
            const payload = {
                est_diameter_min: parseFloat(document.getElementById("est_diameter_min").value),
                est_diameter_max: parseFloat(document.getElementById("est_diameter_max").value),
                relative_velocity: parseFloat(document.getElementById("relative_velocity").value),
                miss_distance: parseFloat(document.getElementById("miss_distance").value),
                sentry_object: document.getElementById("sentry_object").value === "true",
                absolute_magnitude: parseFloat(document.getElementById("absolute_magnitude").value)
            };

            try {
                // Update button text to show loading state
                const submitBtn = form.querySelector('.btn-submit');
                const originalText = submitBtn.textContent;
                submitBtn.textContent = "Analyzing Celestial Telemetry...";
                submitBtn.disabled = true;

                // Call relative backend endpoint
                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    const errorData = await response.json().catch(() => ({}));
                    throw new Error(errorData.detail || `API Error: ${response.status}`);
                }

                const data = await response.json();
                
                // Display result
                resultContainer.style.display = "block";
                resultContainer.className = "result-box"; // Reset classes
                
                const probabilityPercentage = (data.probability * 100).toFixed(2);

                if (data.predicted_category === true) {
                    resultContainer.classList.add("result-danger");
                    resultContainer.innerHTML = `⚠️ HAZARDOUS OBJECT DETECTED!<br><span style="font-size: 16px; font-weight: 400;">Hazard Probability: <strong>${probabilityPercentage}%</strong></span>`;
                } else {
                    resultContainer.classList.add("result-safe");
                    resultContainer.innerHTML = `✅ OBJECT IS SAFE & NON-HAZARDOUS<br><span style="font-size: 16px; font-weight: 400;">Hazard Probability: <strong>${probabilityPercentage}%</strong></span>`;
                }

                // Scroll smoothly to result
                resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

            } catch (error) {
                console.error("Fetch error:", error);
                resultContainer.style.display = "block";
                resultContainer.className = "result-box result-danger";
                resultContainer.innerHTML = `❌ ${error.message || 'Failed to connect to backend API.'}`;
            } finally {
                // Reset button state
                const submitBtn = form.querySelector('.btn-submit');
                if (submitBtn) {
                    submitBtn.textContent = "Run Prediction API";
                    submitBtn.disabled = false;
                }
            }
        });
    }
});