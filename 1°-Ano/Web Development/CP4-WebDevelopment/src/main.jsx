import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css';
import App from './App';
import Sobre from './Pages/Sobre';
import Contato from './Pages/Contato';
import ConteudoPrincipal from './Componentes/ConteudoPrincipal';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      { index: true, element: <ConteudoPrincipal /> },
      { path: 'sobre', element: <Sobre /> },
      { path: 'contato', element: <Contato /> },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

