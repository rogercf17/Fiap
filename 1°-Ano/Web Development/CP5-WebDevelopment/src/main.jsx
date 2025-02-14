import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import Home from './pages/Home.jsx'
import Projetos from './pages/Projetos.jsx'
import Sobre from './pages/Sobre.jsx'
import Contato from './pages/Contato.jsx'
import PageNotFound from './pages/PageNotFound.jsx'
import DetalhesProjetos from './pages/DetalhesProjetos.jsx'
import './index.css'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      {index:true,element:<Home/>},
      {path:'/projetos',element:<Projetos/>},
      {path:'/projetos/:id',element:<DetalhesProjetos/>},
      {path:'/sobre',element:<Sobre/>},
      {path:'/contato',element:<Contato/>},
      {path: '/*',element: <PageNotFound />},
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
