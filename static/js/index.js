document
  .getElementById("search-input")
  .addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      const params = new URLSearchParams(window.location.search);
      params.set("search", this.value);
      window.location.search = params.toString();
    }
  });

document.addEventListener("DOMContentLoaded", () => {
  const likedbutton = document.getElementById("liked-filter");
  const cards = document.querySelectorAll(".recipe-card");

  const likedIds = Object.keys(localStorage)
    .filter((k) => k.startsWith("heart-") && localStorage.getItem(k) === "true")
    .map((k) => k.replace("heart-", ""));

  const params = new URLSearchParams(window.location.search);
  if (params.get("liked")) {
    likedbutton.classList.add("active");
    cards.forEach((card) => {
      const id = card.getAttribute("href").split("/").pop();
      card.style.display = likedIds.includes(id) ? "" : "none";
    });
  }

  likedbutton.addEventListener("click", (e) => {
    e.preventDefault();
    const params = new URLSearchParams();
    params.set("liked", likedIds.join(","));
    window.location.search = params.toString();
  });
});
