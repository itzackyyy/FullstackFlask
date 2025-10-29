import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // La petición usa la ruta /api, que el proxy de Vite redirige al backend
    axios.get('/api/saludo')
      .then(response => {
        setData(response.data.mensaje);
      })
      .catch(error => {
        console.error("Hubo un error al obtener datos:", error);
        setData("Error al conectar con el Backend");
      });
  }, []);

  return (
    <div>
      <h1>Aplicación Fullstack con React</h1>
      <p>Mensaje del Backend: {data || 'Cargando...'}</p>
    </div>
  );
}

export default App;