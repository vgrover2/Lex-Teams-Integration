// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
/*
const { ActivityHandler, MessageFactory } = require('botbuilder');

class EchoBot extends ActivityHandler {
    constructor() {
        super();
        // See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
        this.onMessage(async (context, next) => {
            const replyText = `Echo: ${ context.activity.text }`;
            await context.sendActivity(MessageFactory.text(replyText, replyText));
            // By calling next() you ensure that the next BotHandler is run.
            await next();
        });

        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            const welcomeText = 'Hello and welcome!';
            for (let cnt = 0; cnt < membersAdded.length; ++cnt) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(MessageFactory.text(welcomeText, welcomeText));
                }
            }
            // By calling next() you ensure that the next BotHandler is run.
            await next();
        });
    }
}
*/
const{
    TurnContext, 
    MessageFactory, 
    TeamsInfo, 
    TeamsActivityHandler,
    CardFactory,
    ActionTypes
} = require('botbuilder');
const { LexRuntimeV2Client, RecognizeTextCommand } = require("@aws-sdk/client-lex-runtime-v2");

const AWS_REGION = "";
const AWS_ACCESS_KEY_ID = "";
const AWS_SECRET_ACCESS_KEY = "";

class EchoBot extends TeamsActivityHandler{
    constructor(){
        super();

        this.onMessage(async (context, next) => {
            TurnContext.removeRecipientMention(context.activity);
            await this.callLex(context);
            await next();
        });

        this.onMembersAddedActivity(async (context, next) => {
            context.activity.membersAdded.forEach(async (teamMember) => {
                if(teamMember.id !== context.activity.recipient.id){
                    await context.sendActivity(`Hi, welcome to the team ${ teamMember.givenName } ${ teamMember.surname }`);
                }
            });
            await next();
        });
    }

    async callLex(context){
        const client = new LexRuntimeV2Client({ region: AWS_REGION, credentials: { accessKeyId: AWS_ACCESS_KEY_ID, secretAccessKey: AWS_SECRET_ACCESS_KEY}});

        const params = {
            botId: "",
            botAliasId: "",
            localeId: "en_US",
            sessionId: context.activity.from.id,
            text: context.activity.text.trim()
        };
        try{
            const command = new RecognizeTextCommand(params);
            const response = await client.send(command);

            const message = response.messages[0].content;
            await context.sendActivity(MessageFactory.text(message, message));
        } catch (error) {
            console.error(`Error calling Lex: ${error}`);
            await context.sendActivity(MessageFactory.text("Oops, something went wrong. Please try again later."));
        }
    }
}
module.exports.EchoBot = EchoBot;
