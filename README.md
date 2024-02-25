# reset
Build your application with the `sam build --use-container` command.

```bash
reset$ sam build --use-container
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
reset$ sam local invoke ResetFunction --env-vars env.json
```

```bash
reset$ sam logs -n ResetFunction --stack-name reset --tail
```

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```
