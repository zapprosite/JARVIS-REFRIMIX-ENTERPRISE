---
description: Generate automated tests using TestSprite AI
---

# TestSprite AI Test Generation Workflow

1. **Bootstrap Project**
   - Run `mcp_TestSprite_testsprite_bootstrap`
   - Params: `type="backend"`, `projectPath="{project_root}"`, `testScope="codebase"`

2. **Generate PRD & Plan**
   - Run `testsprite_generate_standardized_prd`
   - Run `testsprite_generate_backend_test_plan`

3. **Generate & Execute Tests**
   - Run `testsprite_generate_code_and_execute`
   - Params: `additionalInstruction="Focus on API endpoints and edge cases."`

4. **Review Results**
   - Check `testsprite_tests/` directory for generated reports.
