import React, { useState } from 'react';
import { NavLink } from "react-router-dom";

export default function Header() {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    return (
        <nav className="w-full bg-gray-800 text-white p-4">
            <div className="container mx-auto flex flex-wrap items-center justify-between">
                <h1 className="text-azulPrincipal text-2xl md:text-3xl lg:text-4xl">
                    <NavLink to="/">RC.F</NavLink>
                </h1>
                
                {/* Hamburger menu for mobile */}
                <button 
                    className="lg:hidden"
                    onClick={() => setIsMenuOpen(!isMenuOpen)}
                >
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>

                {/* Navigation links */}
                <ul className={`${isMenuOpen ? 'block' : 'hidden'} w-full lg:flex lg:w-auto lg:space-x-8 mt-4 lg:mt-0`}>
                    {['Home', 'Projetos', 'Sobre', 'Contato'].map((item) => (
                        <li key={item} className="mb-2 lg:mb-0">
                            <NavLink 
                                to={item === 'Home' ? '/' : `/${item.toLowerCase()}`}
                                className="block hover:text-azulPrincipal transition-colors"
                            >
                                {item}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </div>
        </nav>
    );
}