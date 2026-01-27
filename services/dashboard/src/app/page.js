export default function Home() {
    return (
        <div className="dashboard-container">
            <aside className="sidebar">
                <h2>ZapPRO Admin</h2>
                <nav style={{ marginTop: '20px' }}>
                    <p>Dashboard</p>
                    <p>Tenants</p>
                    <p>Settings</p>
                </nav>
            </aside>

            <main className="main-content">
                <h1>Overview</h1>

                <div className="stats-grid">
                    <div className="card">
                        <h3>Active Tenants</h3>
                        <p style={{ fontSize: '2em', fontWeight: 'bold' }}>3</p>
                    </div>
                    <div className="card">
                        <h3>Total Messages</h3>
                        <p style={{ fontSize: '2em', fontWeight: 'bold' }}>1,240</p>
                    </div>
                    <div className="card">
                        <h3>RAG Accuracy</h3>
                        <p style={{ fontSize: '2em', fontWeight: 'bold' }}>98%</p>
                    </div>
                </div>

                <div className="card">
                    <h3>Recent Activity</h3>
                    <p>No recent activity (Mock Data)</p>
                </div>
            </main>
        </div>
    )
}
