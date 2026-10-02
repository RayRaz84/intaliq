const root={}; require("./engine_test.js")
const fs=require("fs"); const src=fs.readFileSync("./engine_test.js","utf8");
// engine registers on root via (function(root){...})(this|window|globalThis)
