terraform {
  backend "s3" {
    bucket = "nus-iss-equeue-terraform"
    key    = "lambda/listOfBranchesWithClinicId/tfstate"
    region = "us-east-1"
  }
}
