// 1. Importa el módulo Express
const express = require('express');
const app = express();
const port = 3000; // Define el puerto en el que escuchará el servidor

// 2. Define una ruta GET para la raíz ('/')
app.get('/', (req, res) => {
  res.send('¡Hola Mundo!');
});

// 3. Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});