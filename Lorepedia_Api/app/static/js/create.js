
document.addEventListener("DOMContentLoaded", function() {
    const visible = document.getElementById('visible');
    if (visible) {
      visible.addEventListener('change', () => {
        const pass = document.getElementById('password');
        const confirm = document.getElementById('confirm_password');

        const type = visible.checked ? 'text' : 'password';
        
        if (pass) pass.type = type;
        if (confirm) confirm.type = type;
      });
    }

    const registerForm = document.querySelector('form');

    if (registerForm) {
      registerForm.addEventListener('submit', function(event) {
        event.preventDefault();
        registrarUsuario();
      });
    }

    function registrarUsuario() {
      const userName = document.getElementById("username").value.trim();
      const passWord = document.getElementById("password").value.trim();
      const confirmPass = document.getElementById("confirm_password").value.trim();

      if (!userName || !passWord || !confirmPass) {
        alert("Por favor, completa todos los campos.");
        return;
      }

      if (passWord !== confirmPass) {
        alert("Las contraseñas no coinciden. Inténtalo de nuevo.");
        return;
      }
      const users = JSON.parse(localStorage.getItem("users")) || [];

      const existe = users.some(u => u.userName === userName);
      if (existe) {
        alert("Este usuario ya ha sido registrado.");
        return;
      }

      users.push({ userName: userName, password: passWord });
      localStorage.setItem("users", JSON.stringify(users));

      alert("Usuario creado correctamente ✅");
      
      window.location.href = "/login"; 
    }

});

