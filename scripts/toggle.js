document.addEventListener("DOMContentLoaded", () => {
   const toggleSwitch = document.querySelector("#switch");
   const body = document.body;

   if (toggleSwitch.checked) {
      body.classList.add("dark-theme");
      body.classList.remove("light-theme");
   } else {
      body.classList.add("light-theme");
      body.classList.remove("dark-theme");
   }

   toggleSwitch.addEventListener("change", () => {
      if (toggleSwitch.checked) {
         body.classList.add("dark-theme");
         body.classList.remove("light-theme");
      } else {
         body.classList.add("light-theme");
         body.classList.remove("dark-theme");
      }
   });
});