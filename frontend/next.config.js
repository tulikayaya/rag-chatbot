/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: false, // 👈 disables Turbopack and its dev overlay (the "N")
  },
};

module.exports = nextConfig;
