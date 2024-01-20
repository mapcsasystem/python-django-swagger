const { writeFileSync, mkdirSync } = require("fs");
// const { readFileSync } = require("readline");

const dotenv = require("dotenv").config();

const targetPathProd = "./src/environments/environment.prod.ts";
const targetPathDev = "./src/environments/environment.ts";

const environmentContentProd = `
export const environment ={
  production:true,
  BASE_URL:'${process.env.BASE_URL_API_PROD}'
};
`;

const environmentContentDev = `
export const environment ={
  production:false,
  BASE_URL:"${process.env.BASE_URL_API_DEV}"
};
`;

mkdirSync("src/environments", { recursive: true });
writeFileSync(targetPathProd, environmentContentProd);
writeFileSync(targetPathDev, environmentContentDev);

// const html = readFileSync("./dist/blog/browser/index.html", "utf-8");
// console.log(html);
// const a = readFileSync(html, "utf-8");
// console.log(a.path);
