import FormularioContato from "../componentes/FormularioContato"
import { FaRegEnvelope } from "react-icons/fa";
import { BsGeoAlt } from "react-icons/bs";
import { FiPhone } from "react-icons/fi";

export default function Contato() {
    return(
        <section className="
            w-full h-fit
            flex flex-col items-center
            md:w-10/12 md:flex-row md:justify-center
        ">
            <FormularioContato /> 
            <div className="flex flex-col items-center gap-5 mt-5 md:mt-0 md:ml-5">
                <h2 className="text-2xl text-azulPrincipal font-bold md:text-4xl">Vamos Conversar!</h2>
                <div>
                    <ul className="text-white text-base flex flex-col gap-2 md:text-sm md:text-white">
                        <li className="flex items-center gap-2"> 
                            <BsGeoAlt className="text-corLetraFooter"/> São Paulo, SP, Brasil
                        </li>
                        <li className="flex items-center gap-2"> 
                            <FaRegEnvelope className="text-corLetraFooter"/> rogercf16@gmail.com
                        </li>
                        <li className="flex items-center gap-2">
                            <FiPhone className="text-corLetraFooter"/> +55 11998451244
                        </li>
                    </ul>
                </div>
            </div>
        </section>
    )
}
