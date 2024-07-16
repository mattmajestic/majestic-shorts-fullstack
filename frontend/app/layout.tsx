import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Amplify from 'aws-amplify';
import awsconfig from '../auth/aws-config';

const inter = Inter({ subsets: ["latin"] });

// Configure Amplify once the component is loaded on the client-side
if (typeof window !== 'undefined') {
  Amplify.configure(awsconfig);
}

export const metadata: Metadata = {
  title: "Majestic Shorts",
  description: "Framework: Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
