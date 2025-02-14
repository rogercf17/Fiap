/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        azulPrincipal: '#048BF4',
        corLetraFooter: '#646363',
      },
      fontFamily: {
        kanit:['Kanit', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

