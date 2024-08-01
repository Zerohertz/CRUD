const express = require("express");
const bodyParser = require("body-parser");
const userRoutes = require("./routes/userRoutes");

const app = express();
const HOST = "0.0.0.0";
const PORT = process.env.PORT || 1547;

app.use(bodyParser.json());

app.use("/users", userRoutes);

app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
