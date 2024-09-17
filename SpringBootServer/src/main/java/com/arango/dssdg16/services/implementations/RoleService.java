package com.arango.dssdg16.services.implementations;

import com.arango.dssdg16.detos.RoleDTO;
import org.springframework.stereotype.Service;
import services.IRoleService;

@Service("roleService")
public class RoleService implements IRoleService {
    @Override
    public RoleDTO findById(int id) throws Exception {
        return null;
    }
}
