import { useState } from 'react';
import axios from 'axios';
import { Home, Calculator, TrendingUp } from 'lucide-react';

function App() {
  const [formData, setFormData] = useState({
    area_type: "Super built-up Area",
    availability: "Ready To Move",
    location: "Whitefield",
    size: "2 BHK",
    society: "",                    // ← Added society
    total_sqft: 1200,
    bath: 2,
    balcony: 1,
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev, 
      [name]: ["total_sqft", "bath", "balcony"].includes(name) ? Number(value) : value 
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    
    try {
      const response = await axios.post('http://127.0.0.1:8000/predict', formData);
      setPrediction(response.data);
    } catch (err) {
      setError(err.response?.data?.error || err.message || "Prediction failed");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-10">
          <div className="flex justify-center mb-4">
            <Home className="w-16 h-16 text-blue-600" />
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Bengaluru House Price Predictor
          </h1>
          <p className="text-gray-600">AI-Powered Real Estate Valuation</p>
        </div>

        <div className="bg-white rounded-2xl shadow-xl p-8">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium mb-2">Area Type</label>
                <select name="area_type" value={formData.area_type} onChange={handleChange} className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500">
                  <option value="Super built-up Area">Super built-up Area</option>
                  <option value="Built-up Area">Built-up Area</option>
                  <option value="Plot Area">Plot Area</option>
                  <option value="Carpet Area">Carpet Area</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Availability</label>
                <input type="text" name="availability" value={formData.availability} onChange={handleChange} className="w-full p-3 border rounded-lg" />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Location</label>
                <input type="text" name="location" value={formData.location} onChange={handleChange} className="w-full p-3 border rounded-lg" placeholder="e.g. Whitefield" />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Size (BHK)</label>
                <input type="text" name="size" value={formData.size} onChange={handleChange} className="w-full p-3 border rounded-lg" />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Society (Optional)</label>
                <input type="text" name="society" value={formData.society} onChange={handleChange} className="w-full p-3 border rounded-lg" placeholder="e.g. Coomee, Soiewre" />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Total Sqft</label>
                <input type="number" name="total_sqft" value={formData.total_sqft} onChange={handleChange} className="w-full p-3 border rounded-lg" required />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Bathrooms</label>
                <input type="number" name="bath" value={formData.bath} onChange={handleChange} className="w-full p-3 border rounded-lg" required />
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">Balconies</label>
                <input type="number" name="balcony" value={formData.balcony} onChange={handleChange} className="w-full p-3 border rounded-lg" required />
              </div>
            </div>

            <button 
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-4 rounded-xl flex items-center justify-center gap-2 text-lg transition-all disabled:opacity-70"
            >
              <Calculator className="w-5 h-5" />
              {loading ? "Calculating Price..." : "Predict House Price"}
            </button>
          </form>

          {error && <div className="mt-6 p-4 bg-red-100 text-red-700 rounded-xl">{error}</div>}

          {prediction && (
            <div className="mt-10 p-8 bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl border border-green-200 text-center">
              <TrendingUp className="w-12 h-12 text-green-600 mx-auto mb-4" />
              <p className="text-sm text-green-600 font-medium">ESTIMATED PRICE</p>
              <p className="text-6xl font-bold text-green-700 mt-2">
                ₹{prediction.predicted_price}
              </p>
              <p className="text-2xl text-green-600">Lakh INR</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;