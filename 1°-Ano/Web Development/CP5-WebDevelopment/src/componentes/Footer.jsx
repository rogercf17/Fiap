import React from 'react';
import { FaInstagram, FaGithub, FaLinkedin } from "react-icons/fa";

export default function Footer() {
    return (
        <footer className="
            w-full
            py-4
            text-corLetraFooter 
            text-center
            bg-gray-900
            mt-auto
        ">
            <div className="container mx-auto px-4">
                <hr className="
                    w-3/4 
                    mx-auto
                    border-corLetraFooter border-t-2
                    mb-4
                "/>
                <div className="flex gap-4 justify-center mb-4">
                    <a href="https://www.instagram.com/rogercf77/profilecard/?igsh=MzZlbzF5bzBjbnR0" className="transition-all duration-500 hover:text-azulPrincipal">
                        <FaInstagram size={21}/>
                    </a>
                    <a href="https://github.com/rogercf17" className="transition-all duration-500 hover:text-azulPrincipal">
                        <FaGithub size={21}/>
                    </a>
                    <a href="https://www.linkedin.com/in/roger-cardoso-030565212/" className="transition-all duration-500 hover:text-azulPrincipal">
                        <FaLinkedin size={21}/>
                    </a>
                </div>
                <h2 className="text-lg sm:text-xl md:text-2xl mb-2">Me siga nas redes sociais</h2>
                <h4 className="text-xs">©2024 React & Tailwind CSS Portfolio. Roger Cardoso Ferreira</h4>
            </div>
        </footer>
    );
}