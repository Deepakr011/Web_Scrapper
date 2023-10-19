module.exports = async function (message) {
  const accountSid = process.env.TWILIO_ACCOUNT_SID;
  const authToken = process.env.TWILIO_AUTH_TOKEN;
  const client = require("twilio")(accountSid, authToken);
  let result = {};
  try {
    const result = await client.messages.create({
      body: message,
      from: "+12293983881",
      to: "+918088281469",
    });
    result.status = true;
    result.messageSid = message.sid;
  } catch (error) {
    result.status = false;
    result.error = error.message;
  }

  return result;
};
