import './globals.css'

export const metadata = {
    title: 'ZapPRO Dashboard',
    description: 'Admin dashboard for JARVIS-REFRIMIX-ENTERPRISE',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    )
}
