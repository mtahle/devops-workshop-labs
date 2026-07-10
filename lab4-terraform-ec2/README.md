# Lab 4 (Advanced): Provision AWS EC2 with Terraform
**Duration:** 45 minutes  
**Track:** Advanced (after Labs 1–3)  
**Goal:** Provision one EC2 instance in AWS using Terraform in a safe, repeatable workflow.

---

## Learning Objectives

By the end of this lab, students should be able to:
- Initialize and validate Terraform configuration.
- Provision an EC2 instance and a security group.
- Output deployment details and destroy resources safely.

## Prerequisites

- AWS account with IAM permissions for EC2, VPC data lookup, and security groups.
- Terraform CLI installed (`terraform -version`).
- AWS credentials configured locally (recommended: `aws configure` or temporary credentials).

---

## Files in this Lab

```
lab4-terraform-ec2/
├── README.md
├── main.tf.template
├── variables.tf.template
└── terraform.tfvars.example
```

---

## Instructions

### Step 1: Create your Terraform working folder

In your own infra repository:

```bash
mkdir -p infra/terraform
cd infra/terraform
```

Copy `main.tf.template` to `main.tf`, `variables.tf.template` to `variables.tf`, and `terraform.tfvars.example` to `terraform.tfvars`.

### Step 2: Update variables

Set:
- `instance_name`
- `aws_region`
- `instance_type`
- `allowed_cidr` (for SSH access; avoid `0.0.0.0/0` in production)

### Step 3: Initialize and validate

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan
```

### Step 4: Apply and verify

```bash
terraform apply
```

After apply:
- copy the `ec2_public_ip` output
- verify EC2 is running in AWS Console

### Step 5: Cleanup

```bash
terraform destroy
```

---

## Success Criteria (Checkpoint)

- `terraform validate` succeeds.
- `terraform apply` provisions one EC2 instance.
- Outputs show instance ID and public IP.
- `terraform destroy` removes all created resources.

---

## Common Troubleshooting Path

1. Confirm AWS credentials are active for the target region/account.
2. Run `terraform validate` before apply.
3. Check CIDR format and variable values.
4. If apply fails, inspect exact failing resource in logs and AWS Console.

## Reflection Questions

1. Why is IaC safer than manual console provisioning?
2. Which values should be variables vs hardcoded?
3. What additional hardening should be added for production EC2?
