// static/js/script.js

// A simple function to display a confirmation message when a product is added to the cart
function confirmAddToCart() {
    alert("Product added to cart!");
}

// Attach the confirmAddToCart function to the form submit event
document.addEventListener("DOMContentLoaded", function() {
    const addToCartForm = document.querySelector("form.add-to-cart");
    if (addToCartForm) {
        addToCartForm.addEventListener("submit", function(event) {
            event.preventDefault();  // Prevent form from submitting immediately
            confirmAddToCart();  // Display confirmation
            addToCartForm.submit();  // Submit the form after the confirmation
        });
    }
});
