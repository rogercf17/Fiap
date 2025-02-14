import { Link } from "react-router-dom";
function Header() {
    return(
        <nav>
            <ul>
                <li>
                    {/* <a href="#">Home</a> */}
                    <Link to='/'>Home</Link>
                </li>
                <li>
                    <Link to='/sobre'>Sobre</Link>
                </li>
                <li>
                    <Link to='/contato'>Contato</Link>
                </li>
            </ul>
        </nav>
    );
}
export default Header;