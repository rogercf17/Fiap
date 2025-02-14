import { Link } from "react-router-dom";
import styles from './Header.module.css';


const estiloTitulo = {
	color: 'blue',
	backgroundColor: 'white'
}

/*isAdmin ? estiloTitulo: undefined -- adiciona style por condição se for admin*/
function Header() {
  return (
    <header>
      <h1 style ={estiloTitulo}>Meu site</h1>
	  <h2 className={styles.titulo}>Subtítulo</h2>
      <nav>
      <ul>
		<li>
			<Link to='/'>Home</Link>
		</li>
    <li>
			<Link to='/sobre'>Sobre</Link>
		</li>
		<li>
			<Link to='/servicos'>Serviços</Link>
		</li>
    <li>
			<Link to='/contato'>Contato</Link>
		</li>
	</ul>
        </nav>
    </header>
  );
}

export default Header;
