import type { Metadata } from "next";
import "./globals.css";

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: "Consultora de gestión clínica | Equia",
  description: "Consultoría especializada en gestión clínica, operaciones, analítica y tecnología para organizaciones de salud.",
  openGraph: {
    title: "Gestión clínica e innovación en salud",
    description: "Experiencia clínica y tecnología para transformar la gestión en salud.",
    images: [{ url: "/og.png", width: 1200, height: 630 }],
    locale: "es_CL",
    type: "website"
  },
  twitter: { card: "summary_large_image", images: ["/og.png"] }
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
