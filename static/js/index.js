document
  .getElementById("search-input")
  .addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      const params = new URLSearchParams(window.location.search);
      params.set("search", this.value);
      window.location.search = params.toString();
    }
  });
