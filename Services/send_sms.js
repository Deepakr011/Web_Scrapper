module.exports = async function (message) {
  const accountSid = process.env.TWILIO_ACCOUNT_SID;
  const authToken = process.env.TWILIO_AUTH_TOKEN;
  const client = require("twilio")(accountSid, authToken);
  let result = {};
  try {
    const result = await client.messages.create({
      body: message,
      from: "+12295365102",
      to: "+918088281469",
    });
  } catch (error) {
    throw new Error(error.message);
  }

  return result;
};
