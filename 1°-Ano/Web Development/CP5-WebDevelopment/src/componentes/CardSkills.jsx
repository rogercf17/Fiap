import { FaFigma, FaPython, FaNodeJs, FaPhp, FaJs, FaHtml5,  FaCss3, FaReact, FaBootstrap, FaSass, FaGitAlt } from "react-icons/fa"
import { RiTailwindCssFill } from "react-icons/ri"
import { SiMysql, SiArduino } from "react-icons/si"


export default function CardSkills() {
    return(
        <div className="
            w-full flex flex-col 
            justify-center items-center 
            gap-2
        ">
            <h2 className="text-white text-3xl">Skills</h2>
            <div className="
                w-10/12 h-28
                flex flex-col items-center
                gap-1
                p-3
                bg-slate-950
                rounded-ss-md rounded-e-3xl
                shadow-md
            ">
                <h3 className="text-white self-center text-xl mb-1 italic">FrontEnd</h3>
                <div className="flex gap-2">
                    <FaHtml5 fill="#e86c00" size={38} />
                    <FaCss3 fill="#0100c8" size={38} />
                    <FaBootstrap fill="#890079" size={38} />
                    <FaReact fill="#00e2f1" size={38} />
                    <RiTailwindCssFill fill="#07bcff" size={38} />
                    <FaSass  fill="#ff36e1" size={38} />
                </div>
            </div>
            <div className="
                w-10/12 h-28
                flex flex-col items-center
                gap-1
                p-3
                bg-slate-950 
                rounded-ss-md rounded-e-3xl
                shadow-md
            ">
                <h3 className="text-white self-center text-xl mb-1 italic">BackEnd</h3>
                <div className="flex gap-2">
                    <FaPhp fill="#8300bd" size={38} />
                    <FaJs fill="#f2fe00" size={38} />
                    <FaPython fill="#0d0080" size={38} />
                    <FaNodeJs fill="#00ab17" size={38} />
                </div>
            </div>
            <div className="
                w-10/12 h-28
                flex flex-col items-center
                gap-1
                p-3
                bg-slate-950 
                rounded-ss-md rounded-e-3xl
                shadow-md
            ">
                <h3 className="text-white self-center text-xl mb-1 italic">Dados</h3>
                <div className="flex gap-2">
                    <SiMysql fill="#FFF" size={38}/>
                </div>
            </div>
            <div className="
                w-10/12 h-28
                flex flex-col items-center
                gap-1
                p-3
                bg-slate-950 
                rounded-ss-md rounded-e-3xl
                shadow-md
            ">
                <h3 className="text-white self-center text-xl mb-1 italic">Outros</h3>
                <div className="flex gap-2">
                    <FaGitAlt fill="#e86c00" size={38}/>
                    <SiArduino fill="#2c8fff" size={38}/>
                    <FaFigma fill="#FFF" size={38}/>   
                </div>
            </div>
        </div>
    )
}