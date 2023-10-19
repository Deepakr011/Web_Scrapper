const { application } = require("express");
const cheerio = require("cheerio");
require("dotenv").config();
const sendSMS = require("./Services/send_sms");
const sendGmail = require("./Services/send_gmail");

const PORT = process.env.PORT || 5000;

function dataExtracter(html, market) {
  const $ = cheerio.load(html);
  const searchText = market;
  const $targetTRs = $("tr").filter((index, element) => {
    return (
      $(element)
        .find("td")
        .filter((idx, td) => {
          return $(td).text() === searchText;
        }).length > 0
    );
  });
  let str = "";
  $targetTRs.each((index, element) => {
    const result = $(element)
      .html()
      .replace(/\s+|\n|<[^>]*>/g, " ")
      .split(" ")
      .filter((item) => item.trim() !== "");
    if (result[2] === "Rashi") {
      str = `${result[0]}:${result[1]}\nRS:${result[5]}`;
    }
  });
  return str;
}

async function fetchData() {
  try {
    const response = await fetch(process.env.KRISHI_MARKET_URL);
    const html = await response.text();
    const message = `${dataExtracter(html, "SAGAR")}\n${dataExtracter(
      html,
      "SHIVAMOGGA"
    )}`;
    const smsResult = await sendSMS(message);
    if (!smsResult.status) {
      throw new Error(smsResult.error);
    }
    fetchData();
  } catch (error) {
    console.log(error.message);
    await sendGmail("magowtham7@gmail.com", error.message);
  }
}
function timeSheduler() {
  const now = new Date();
  const targetDate = new Date(
    now.getFullYear(),
    now.getMonth(),
    now.getDate(),
    2,
    15,
    0
  );
  let delay = targetDate - now;
  if (delay < 0) {
    delay += 24 * 60 * 60 * 1000;
  }
  setTimeout(fetchData, delay);
}
timeSheduler();
application.listen(PORT, () => {
  console.log(`server running @ port : ${PORT}`);
});
