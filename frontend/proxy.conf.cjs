const PREFIX_RE = /^\/@[^/]+\/[^/]+\/apps\/[^/]+/;

module.exports = {
  "/api": {
    target: "http://localhost:8000",
    secure: false,
    changeOrigin: true,
    logLevel: "debug",
  },
  "^/@[^/]+/[^/]+/apps/[^/]+/api": {
    target: "http://localhost:8000",
    secure: false,
    changeOrigin: true,
    logLevel: "debug",
    pathRewrite: (path) => path.replace(PREFIX_RE, ""),
  },
};
