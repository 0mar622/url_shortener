import React, { useState, useEffect } from 'react';
import { Link2, BarChart3, Copy, Check } from 'lucide-react';

export default function URLShortener() {
  const [activeTab, setActiveTab] = useState('shorten');
  const [longUrl, setLongUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [stats, setStats] = useState([]);
  const [copied, setCopied] = useState(false);

  const API_BASE = 'https://url-shortener-main.onrender.com';

  const handleShorten = async () => {
    if (!longUrl) return;
    
    setError('');
    setShortUrl('');
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE}/shorten`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ long_url: longUrl }),
      });

      if (!response.ok) throw new Error('Failed to shorten URL');

      const data = await response.json();
      setShortUrl(data.short_url);
      setLongUrl('');
    } catch (err) {
      setError('Failed to shorten URL. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const fetchStats = async () => {
    try {
      const response = await fetch(`${API_BASE}/stats`);
      if (!response.ok) throw new Error('Failed to fetch stats');
      const data = await response.json();
      setStats(data.stats || []);
    } catch (err) {
      setError('Failed to load stats');
    }
  };

  useEffect(() => {
    if (activeTab === 'stats') {
      fetchStats();
    }
  }, [activeTab]);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleShorten();
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">🔗 URL Shortener</h1>
          <p className="text-gray-600">Shorten your links and track analytics</p>
        </div>

        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex gap-4 border-b pb-4 mb-6">
            <button
              onClick={() => setActiveTab('shorten')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg transition ${
                activeTab === 'shorten'
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              <Link2 size={20} />
              Shorten URL
            </button>
            <button
              onClick={() => setActiveTab('stats')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg transition ${
                activeTab === 'stats'
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              <BarChart3 size={20} />
              Analytics
            </button>
          </div>

          {activeTab === 'shorten' && (
            <div>
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Enter URL to shorten
                  </label>
                  <input
                    type="url"
                    value={longUrl}
                    onChange={(e) => setLongUrl(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="https://example.com/very-long-url"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <button
                  onClick={handleShorten}
                  disabled={loading || !longUrl}
                  className="w-full bg-blue-500 text-white py-3 rounded-lg font-medium hover:bg-blue-600 transition disabled:bg-gray-400"
                >
                  {loading ? 'Shortening...' : 'Shorten URL'}
                </button>
              </div>

              {error && (
                <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
                  {error}
                </div>
              )}

              {shortUrl && (
                <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
                  <p className="text-sm text-gray-600 mb-2">Your shortened URL:</p>
                  <div className="flex items-center gap-2">
                    <input
                      type="text"
                      value={shortUrl}
                      readOnly
                      className="flex-1 px-3 py-2 bg-white border border-gray-300 rounded"
                    />
                    <button
                      onClick={copyToClipboard}
                      className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
                    >
                      {copied ? <Check size={18} /> : <Copy size={18} />}
                      {copied ? 'Copied!' : 'Copy'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'stats' && (
            <div>
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold text-gray-800">Link Analytics</h2>
                <button
                  onClick={fetchStats}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
                >
                  Refresh
                </button>
              </div>

              {stats.length === 0 ? (
                <div className="text-center py-8 text-gray-500">
                  No links created yet. Create your first short URL!
                </div>
              ) : (
                <div className="space-y-3">
                  {stats.map((item, index) => (
                    <div
                      key={index}
                      className="p-4 bg-gray-50 rounded-lg border border-gray-200 hover:shadow-md transition"
                    >
                      <div className="flex justify-between items-start mb-2">
                        <div className="flex-1 mr-4">
                          <p className="text-sm font-medium text-blue-600 break-all">
                            /{item.short_code}
                          </p>
                          <p className="text-sm text-gray-500 break-all mt-1">
                            → {item.long_url}
                          </p>
                        </div>
                        <div className="text-right">
                          <p className="text-2xl font-bold text-gray-800">{item.clicks}</p>
                          <p className="text-xs text-gray-500">clicks</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>

        <div className="text-center text-sm text-gray-600">
          <p>Built with React + Flask + PostgreSQL</p>
        </div>
      </div>
    </div>
  );
}
