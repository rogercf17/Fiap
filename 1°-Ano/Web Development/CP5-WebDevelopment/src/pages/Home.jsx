import React from 'react';
import ImageHero from "/image-hero.png";
import Footer from "../componentes/Footer";
import EfeitoTexto from "../componentes/EfeitoTexto";

export default function Home() {
    const handleDownload = () => {
        const url = "/Roger.docx";
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "Roger.docx");
        document.body.appendChild(link);
        link.click();
        link.remove();
    };

    return (
        <div className="flex flex-col min-h-screen">
            <main className="flex-grow">
                <section className="
                    w-11/12 
                    mx-auto 
                    py-8 
                    flex 
                    flex-col 
                    items-center 
                    gap-8
                    md:flex-row 
                    md:justify-between 
                    md:items-center 
                    lg:gap-16
                ">
                    <div className="text-white space-y-4 text-center md:text-left">
                        <div className="flex items-center justify-center md:justify-start gap-2">
                            <span className="animate-spin text-2xl md:text-3xl lg:text-4xl">😊</span>
                            <h2 className="font-bold text-2xl md:text-3xl lg:text-4xl text-azulPrincipal">
                                Olá, eu sou o Roger
                            </h2>
                        </div>
                        <EfeitoTexto 
                            texto="Enngenheiro de Software" 
                            velocidade={100} 
                            className="text-lg md:text-xl lg:text-2xl"
                        />
                        <button 
                            className="
                                w-full md:w-auto 
                                px-4 py-2 
                                bg-azulPrincipal 
                                text-sm md:text-base
                                hover:bg-blue-600 
                                transition-colors
                            " 
                            onClick={handleDownload}
                        >
                            Download CV
                        </button>
                    </div>
                    <div className="mt-8 md:mt-0">
                        <img 
                            src={ImageHero} 
                            alt="Imagem do Hero" 
                            className="
                                h-48 w-48
                                md:h-56 md:w-56
                                lg:h-72 lg:w-72
                                mx-auto
                            "
                        />
                    </div>
                </section>
            </main>
            <Footer />
        </div>
    );
}