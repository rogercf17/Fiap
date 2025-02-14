import { useEffect, useState } from "react";

export default function EfeitoTexto({ texto, velocidade }) {
    const [textoVisivel, setTextoVisivel] = useState('')

    useEffect(() => {
        let index = 0; // Índice inicial

        const adicionarLetra = () => {
            if (index < texto.length) {
                setTextoVisivel((valorAtual) => valorAtual + texto.charAt(index))
                index++
                setTimeout(adicionarLetra, velocidade)
            }
        }

        const timeout = setTimeout(adicionarLetra, velocidade)

        return () => clearTimeout(timeout)
    }, [texto, velocidade])

    return <h3 className="typed-text text-2xl">{textoVisivel}</h3>
}
