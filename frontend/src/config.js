const rawApiBase = import.meta.env.VITE_API_BASE || "http://localhost:5000"

export const API_BASE = rawApiBase.replace(/\/$/, "")
