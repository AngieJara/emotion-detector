document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const textInput = document.querySelector("textarea[name='text_to_analyse']");

  if (!form || !textInput) {
    return;
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const textToAnalyse = textInput.value.trim();

    if (!textToAnalyse) {
      window.location.href = "/";
      return;
    }

    window.location.href = `/?text_to_analyse=${encodeURIComponent(textToAnalyse)}`;
  });
});
