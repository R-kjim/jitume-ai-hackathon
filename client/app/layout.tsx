import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Jitume AI Hackathon',
  description: 'AI Workflow Dashboard',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="h-screen w-screen overflow-hidden bg-[#0d0e12] text-white">
        {children}
      </body>
    </html>
  );
}
