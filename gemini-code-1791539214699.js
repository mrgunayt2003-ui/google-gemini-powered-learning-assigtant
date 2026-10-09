async function sendQuery(userText) {
  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userText, emotion: 'focused' })
  });
  const data = await response.json();
  console.log("EduGenie Response:", data.response);
}