---
description: "Workflow de Release para Coolify"
---

# Release Workflow

1. **Bump Version**
   - `npm version patch` ou atualize `VERSION` file.
   - Commit com tag `vX.Y.Z`.

2. **Push**
   - `git push origin main --tags`

3. **Coolify Webhook**
   - O repositório deve estar configurado no Coolify com "Autodeploy" ativado para a branch `main`.
   - O webhook do GitHub/Gitea notificará o Coolify.

4. **Verify**
   - Acesse o dashboard do Coolify.
   - Verifique se o build passou.
   - Verifique os logs do container novo.
