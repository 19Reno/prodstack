package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestDockerInfra(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../terraform",
        NoColor: true,
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    privateNetwork := terraform.Output(t, terraformOptions, "private_network_name")
    assert.Equal(t, "prodstack-private-tf", privateNetwork)

    publicNetwork := terraform.Output(t, terraformOptions, "public_network_name")
    assert.Equal(t, "prodstack-public-tf", publicNetwork)

    container := terraform.Output(t, terraformOptions, "container_name")
    assert.Equal(t, "tf-app", container)
}
