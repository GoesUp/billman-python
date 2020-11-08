export const logoNegative = ['608 134', `
  <defs>
    <filter id="editing-hole" x="-100%" y="-100%" width="300%" height="300%">
      <feFlood flood-color="#000" result="black"></feFlood>
      <feMorphology operator="dilate" radius="2" in="SourceGraphic" result="erode"></feMorphology>
      <feGaussianBlur in="erode" stdDeviation="4" result="blur"></feGaussianBlur>
      <feOffset in="blur" dx="2" dy="2" result="offset"></feOffset>
      <feComposite operator="atop" in="offset" in2="black" result="merge"></feComposite>
      <feComposite operator="in" in="merge" in2="SourceGraphic" result="inner-shadow"></feComposite>
    </filter>
  </defs>
  <g filter="url(#editing-hole)">
    <g transform="translate(90.63999632000923, 95.9921875) scale(1.7)"">
      <path
        d="M0.45-0.32L0.45-0.32L8.51-42.24L8.51-42.24Q16.06-42.88 20.93-42.88L20.93-42.88L20.93-42.88Q25.79-42.88 28.93-42.46L28.93-42.46L28.93-42.46Q32.06-42.05 34.18-40.96L34.18-40.96L34.18-40.96Q38.40-38.91 38.40-33.28L38.40-33.28L38.40-33.28Q38.40-30.02 35.58-27.26L35.58-27.26L35.58-27.26Q32.96-24.77 30.08-24.19L30.08-24.19L30.08-24.19Q33.15-23.68 35.33-21.38L35.33-21.38L35.33-21.38Q37.63-18.94 37.63-15.17L37.63-15.17L37.63-15.17Q37.63-7.87 32.19-3.62L32.19-3.62L32.19-3.62Q26.75 0.64 16.06 0.64L16.06 0.64L16.06 0.64Q8.70 0.64 0.45-0.32ZM17.86-20.61L14.66-4.03L14.66-4.03Q15.23-3.97 15.36-3.97L15.36-3.97L15.94-3.97L15.94-3.97Q21.18-3.97 23.42-7.42L23.42-7.42L23.42-7.42Q25.09-10.11 25.09-15.04L25.09-15.04L25.09-15.04Q25.09-17.66 23.39-19.07L23.39-19.07L23.39-19.07Q21.70-20.48 17.86-20.61L17.86-20.61ZM27.58-33.22L27.58-33.22L27.58-33.22Q27.58-38.53 22.46-38.53L22.46-38.53L21.89-38.53L21.89-38.53Q21.63-38.53 21.25-38.46L21.25-38.46L18.69-24.96L19.33-24.96L19.33-24.96Q27.58-25.15 27.58-33.22ZM57.22-3.52L57.22-3.52L57.22-3.52Q55.23 1.28 48.90 1.28L48.90 1.28L48.90 1.28Q45.63 1.28 43.58-0.96L43.58-0.96L43.58-0.96Q41.86-2.94 41.86-4.93L41.86-4.93L41.86-4.93Q41.86-10.11 44.22-20.22L44.22-20.22L46.59-32.64L59.58-33.92L55.68-13.70L55.68-13.70Q54.59-8.96 54.59-7.30L54.59-7.30L54.59-7.30Q54.59-3.65 57.22-3.52ZM47.74-41.54L47.74-41.54L47.74-41.54Q47.74-44.03 49.82-45.38L49.82-45.38L49.82-45.38Q51.90-46.72 54.91-46.72L54.91-46.72L54.91-46.72Q57.92-46.72 59.74-45.38L59.74-45.38L59.74-45.38Q61.57-44.03 61.57-41.54L61.57-41.54L61.57-41.54Q61.57-39.04 59.55-37.76L59.55-37.76L59.55-37.76Q57.54-36.48 54.53-36.48L54.53-36.48L54.53-36.48Q51.52-36.48 49.63-37.76L49.63-37.76L49.63-37.76Q47.74-39.04 47.74-41.54ZM77.95-3.52L77.95-3.52L77.95-3.52Q75.97 1.28 69.63 1.28L69.63 1.28L69.63 1.28Q66.43 1.28 64.38-0.96L64.38-0.96L64.38-0.96Q62.72-2.82 62.72-4.93L62.72-4.93L62.72-4.93Q62.72-9.73 64.96-20.22L64.96-20.22L69.63-44.80L82.62-46.08L76.42-13.70L76.42-13.70Q75.33-8.96 75.33-7.30L75.33-7.30L75.33-7.30Q75.33-3.65 77.95-3.52ZM98.69-3.52L98.69-3.52L98.69-3.52Q96.70 1.28 90.37 1.28L90.37 1.28L90.37 1.28Q87.17 1.28 85.12-0.96L85.12-0.96L85.12-0.96Q83.46-2.82 83.46-4.93L83.46-4.93L83.46-4.93Q83.46-9.73 85.70-20.22L85.70-20.22L90.37-44.80L103.36-46.08L97.15-13.70L97.15-13.70Q96.06-8.96 96.06-7.30L96.06-7.30L96.06-7.30Q96.06-3.65 98.69-3.52ZM150.21 1.28L150.21 1.28L150.21 1.28Q142.46 1.28 142.46-4.74L142.46-4.74L142.46-4.74Q142.46-7.36 143.58-12.45L143.58-12.45L143.58-12.45Q144.70-17.54 145.09-19.58L145.09-19.58L145.09-19.58Q145.98-24.26 145.98-25.73L145.98-25.73L145.98-25.73Q145.98-28.99 143.55-28.99L143.55-28.99L143.55-28.99Q141.95-28.99 140.42-26.78L140.42-26.78L140.42-26.78Q138.88-24.58 138.18-20.16L138.18-20.16L134.21 0L121.73 1.28L125.18-16.13L125.18-16.13Q125.76-19.01 126.27-22.27L126.27-22.27L126.27-22.27Q126.78-25.54 126.78-26.05L126.78-26.05L126.78-26.05Q126.78-28.99 124.61-28.99L124.61-28.99L124.61-28.99Q123.14-28.99 121.54-26.82L121.54-26.82L121.54-26.82Q119.94-24.64 119.04-20.16L119.04-20.16L115.14 0L102.53 1.28L109.25-32.64L119.68-33.92L118.59-27.46L118.59-27.46Q120.26-30.91 123.33-32.42L123.33-32.42L123.33-32.42Q126.40-33.92 131.20-33.92L131.20-33.92L131.20-33.92Q133.95-33.92 135.74-32.58L135.74-32.58L135.74-32.58Q137.54-31.23 138.11-29.06L138.11-29.06L138.11-29.06Q139.20-31.30 141.98-32.61L141.98-32.61L141.98-32.61Q144.77-33.92 148.19-33.92L148.19-33.92L148.19-33.92Q151.62-33.92 153.31-33.18L153.31-33.18L153.31-33.18Q155.01-32.45 156.03-31.23L156.03-31.23L156.03-31.23Q157.76-28.99 157.76-24.90L157.76-24.90L157.76-24.90Q157.76-20.86 156.03-12.48L156.03-12.48L156.03-12.48Q155.14-8.38 155.14-6.88L155.14-6.88L155.14-6.88Q155.14-5.38 156-4.48L156-4.48L156-4.48Q156.86-3.58 158.14-3.46L158.14-3.46L158.14-3.46Q157.50-1.28 155.30 0L155.30 0L155.30 0Q153.09 1.28 150.21 1.28ZM165.86-1.92L165.86-1.92L165.86-1.92Q164.35-3.58 163.68-6.21L163.68-6.21L163.68-6.21Q163.01-8.83 163.01-13.12L163.01-13.12L163.01-13.12Q163.01-17.41 164.48-21.31L164.48-21.31L164.48-21.31Q165.95-25.22 168.64-28.03L168.64-28.03L168.64-28.03Q174.14-33.92 183.23-33.92L183.23-33.92L183.23-33.92Q186.50-33.92 188.86-32.83L188.86-32.83L199.81-33.92L195.07-8.96L195.07-8.96Q194.88-8.19 194.88-6.78L194.88-6.78L194.88-6.78Q194.88-5.38 195.74-4.48L195.74-4.48L195.74-4.48Q196.61-3.58 197.89-3.46L197.89-3.46L197.89-3.46Q197.25-1.28 194.91 0L194.91 0L194.91 0Q192.58 1.28 189.95 1.28L189.95 1.28L189.95 1.28Q187.33 1.28 185.57 0.29L185.57 0.29L185.57 0.29Q183.81-0.70 183.30-2.37L183.30-2.37L183.30-2.37Q182.27-0.77 180.10 0.26L180.10 0.26L180.10 0.26Q177.92 1.28 175.01 1.28L175.01 1.28L175.01 1.28Q172.10 1.28 169.73 0.51L169.73 0.51L169.73 0.51Q167.36-0.26 165.86-1.92ZM179.36-27.90L179.36-27.90L179.36-27.90Q178.62-26.75 177.98-24.80L177.98-24.80L177.98-24.80Q177.34-22.85 176.29-17.63L176.29-17.63L176.29-17.63Q175.23-12.42 175.23-8.70L175.23-8.70L175.23-8.70Q175.23-4.99 175.81-3.90L175.81-3.90L175.81-3.90Q176.38-2.82 177.41-2.82L177.41-2.82L177.41-2.82Q179.46-2.82 180.96-4.77L180.96-4.77L180.96-4.77Q182.46-6.72 183.04-10.18L183.04-10.18L186.43-28.93L186.43-28.93Q185.09-30.08 183.52-30.08L183.52-30.08L183.52-30.08Q181.95-30.08 181.02-29.57L181.02-29.57L181.02-29.57Q180.10-29.06 179.36-27.90ZM230.34 1.28L230.34 1.28L230.34 1.28Q222.59 1.28 222.59-4.74L222.59-4.74L222.59-4.74Q222.66-6.40 223.17-9.22L223.17-9.22L224.32-15.10L224.32-15.10Q226.05-23.42 226.05-25.28L226.05-25.28L226.05-25.28Q226.05-28.99 223.87-28.99L223.87-28.99L223.87-28.99Q220.22-28.99 218.30-19.46L218.30-19.46L214.53 0L201.66 1.28L208.32-32.70L218.82-33.92L217.79-27.65L217.79-27.65Q220.80-33.92 230.02-33.92L230.02-33.92L230.02-33.92Q234.50-33.92 236.38-32.03L236.38-32.03L236.38-32.03Q238.27-30.14 238.27-25.92L238.27-25.92L238.27-25.92Q238.27-21.95 236.22-12.67L236.22-12.67L236.22-12.67Q235.26-8.51 235.26-6.94L235.26-6.94L235.26-6.94Q235.26-5.38 236.13-4.48L236.13-4.48L236.13-4.48Q236.99-3.58 238.27-3.46L238.27-3.46L238.27-3.46Q237.63-1.28 235.42 0L235.42 0L235.42 0Q233.22 1.28 230.34 1.28Z"
        fill="#eee"></path>
    </g>
  </g>
  <style>text {
    font-size: 150px;
    font-family: Arial Black;
    dominant-baseline: central;
    text-anchor: middle;
    }
  </style>
`]
