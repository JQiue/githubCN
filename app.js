import { EdgeWebstoreClient } from "@plasmo-corp/ewu";
import compressing from "compressing";
import dotenv from "dotenv";

dotenv.config();
console.log(process.env);
compressing.zip.compressDir("src/", "dist.zip");

const client = new EdgeWebstoreClient({
  productId: process.env.PRODUCT_ID,
  clientId: process.env.CLIENT_ID,
  clientSecret: process.env.CLIENT_SECRET,
  accessTokenUrl: process.env.ACCESS_TOKEN_URL,
});

const data = await client.submit({
  filePath: "./dist.zip",
  notes: "Developer notes",
});
