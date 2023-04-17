const modal = document.querySelector(".modal");
const formRegister = document.getElementById("form");

formRegister.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(formRegister);
  const data = Object.fromEntries(formData);

  register(data);
});

async function register(data) {
  const response = await fetch("/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const responseJson = await response.json();

  if (responseJson.hasError) {
    modal.classList.remove("hidden");
    const modalTitle = document.querySelector(".modal__title");
    modalTitle.textContent = "Error";
    const modalText = document.querySelector(".modal__text");
    modalText.textContent = responseJson.message;

    const modalBtn = document.querySelector(".modal__btn");
    modalBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  } else {
    modal.classList.remove("hidden");
    const modalTitle = document.querySelector(".modal__title");
    modalTitle.textContent = "Success";

    const modalText = document.querySelector(".modal__text");
    modalText.textContent = responseJson.message;

    const modalBtn = document.querySelector(".modal__btn");
    modalBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  }
}
