const form = document.getElementById("symptomForm");
const advicePanel = document.getElementById("advicePanel");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const response = await fetch("/", {
        method: "POST",
        body: formData
    });
    const data = await response.json();
    advicePanel.innerHTML = `<p><strong>AI Advice:</strong> ${data.advice}</p>
                             <p><strong>Severity:</strong> ${data.severity}</p>`;
});
