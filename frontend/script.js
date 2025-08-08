const API_BASE = 'https://url-shorten-16li.onrender.com'; // Replace with actual backend URL

async function shortenUrl() {
  const longUrl = document.getElementById('longUrl').value.trim();
  const resultDiv = document.getElementById('result');

  resultDiv.innerHTML = ''; // Clear previous result

  if (!longUrl) {
    resultDiv.textContent = 'Please enter a valid URL.';
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/shorten`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ originalUrl: longUrl })
    });

    const data = await response.json();

    if (response.ok && data.shortUrl) {
      resultDiv.innerHTML = `
        ✅ Shortened URL: <a href="${data.shortUrl}" target="_blank">${data.shortUrl}</a>
      `;
    } else {
      resultDiv.textContent = data.message || 'Failed to shorten URL.';
    }
  } catch (error) {
    console.error('Error:', error);
    resultDiv.textContent = 'Server error. Please try again later.';
  }
}