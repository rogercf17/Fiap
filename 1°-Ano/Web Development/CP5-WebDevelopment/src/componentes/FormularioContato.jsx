export default function FormularioContato() {
    return(
        <form className="
                flex flex-col gap-4 items-center justify-center
                w-full
                p-5
                text-corLetraFooter text-sm
                md:w-2/3
            ">
                <input type="text" id="nome" placeholder="Nome Completo" className="w-full p-2 rounded-xl md:w-5/12"/>
                <input type="email" id="email" placeholder="Email" className="w-full p-2 rounded-xl md:w-5/12"/>
                <input type="tel" id="telefone" placeholder="N° de Celular" className="w-full p-2 rounded-xl md:w-5/12"/>
                <textarea id="mensagem" cols={4} rows={4} placeholder="Mensagem" className="w-full p-2 resize-none rounded-xl md:w-5/12"></textarea>
                <button type="button" className="w-24 h-8 bg-azulPrincipal text-white rounded-md">Enviar</button>
        </form>
    )
}
