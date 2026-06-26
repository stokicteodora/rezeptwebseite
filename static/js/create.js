//
// File: create.js
// Author: Teodora Stokic
// Date: 26.06.2026
// Version: 1.2
// Description: Adds ingredients and steps dynamically in the recipe form.
//

// Adds a new empty ingredient row to the ingredients list
function addIngredient() {
  const div = document.createElement("div");
  div.className = "ingredient-row";
  div.innerHTML = `
        <input type="text" name="ingredient_name[]" placeholder="Name">
        <input type="number" name="ingredient_quantity[]" placeholder="Menge">
        <input type="text" name="ingredient_unit[]" placeholder="Einheit (g, ml, EL...)">
    `;
  document.getElementById("ingredients").appendChild(div);
}

// Adds a new empty step textarea to the steps list
function addStep() {
  const div = document.createElement("div");
  div.className = "step-row";
  div.innerHTML = `<textarea name="step_description[]" placeholder="Schritt"></textarea>`;
  document.getElementById("steps").appendChild(div);
}
