import express from "express";

const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.json({
    app: "proj1",
    environment: process.env.APP_ENV || "development"
  });
});

app.listen(port, () => {
  console.log(`proj1 listening on ${port}`);
});
