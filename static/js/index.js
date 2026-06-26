//
// File: index.js
// Author: Teodora Stokic
// Date: 26.06.2026
// Version: 1.2
// Description: Handles search functionality and "liked recipes" filter
// using localStorage and URL parameters on the recipe overview page.
//

// Search: pressing Enter updates the URL with the search term
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
  // Collect all recipe IDs marked as liked in localStorage
  const likedIds = Object.keys(localStorage)
    .filter((k) => k.startsWith("heart-") && localStorage.getItem(k) === "true")
    .map((k) => k.replace("heart-", ""));
  // If the liked filter is active, show only liked recipes
  const params = new URLSearchParams(window.location.search);
  if (params.get("liked")) {
    likedbutton.classList.add("active");
    cards.forEach((card) => {
      const id = card.getAttribute("href").split("/").pop();
      card.style.display = likedIds.includes(id) ? "" : "none";
    });
  }
  // Clicking the liked button adds liked IDs to the URL and reloads
  likedbutton.addEventListener("click", (e) => {
    e.preventDefault();
    const params = new URLSearchParams();
    params.set("liked", likedIds.join(","));
    window.location.search = params.toString();
  });
});
